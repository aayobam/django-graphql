import graphene
from graphql import GraphQLError
from apps.schema.models import Book
from graphene_django import DjangoObjectType



# This serves purpose just as serializers in django rest framework
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"


# This helps to fetch data from the server/database(List and Details views)
class BookQuery(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book_details = graphene.Field(BookType, book_id=graphene.ID())

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book_details(self, info, book_id, **kwargs):
        return Book.objects.get(id=book_id)


class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int()

    def __str__(self):
        return self.title


# create new books
class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book( 
            title=book_data.title,
            author=book_data.author,
            year_published=book_data.year_published,
            review=book_data.review
        )
        book_instance.save()
        return CreateBook(book=book_instance)


# update book instance
class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book.objects.get(pk=book_data.id)
        if book_instance:
            book_instance.title = book_data.title
            book_instance.author = book_data.author
            book_instance.year_published = book_data.year_published
            book_instance.review = book_data.review
            book_instance.save()
            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)


# delete book
class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        if book_instance:
            book_instance.delete()
            return DeleteBook(book=None)
        raise GraphQLError("book instance not found")

