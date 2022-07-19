import graphene
from apps.schema.schema import (
    BookQuery,
    CreateBook,
    UpdateBook,
    DeleteBook
)


class Query(BookQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)