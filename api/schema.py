import graphene
from graphene_django import DjangoObjectType
from api.models import Book



# This serves purpose just as serializers in django rest framework
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"


# This helps to fetch data from the server/database(List and Details views)
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(Book, book_id=graphene.ID())

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, book_id):
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
    class Arguements:
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


# update book
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
        book_instance.delete()
        return None


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)