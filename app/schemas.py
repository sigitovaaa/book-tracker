from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    name: str
    country: str | None = None


class AuthorCreate(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class GenreBase(BaseModel):
    title: str


class GenreCreate(GenreBase):
    pass


class GenreOut(GenreBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: str
    year: int | None = None
    author_id: int
    genre_id: int


class BookCreate(BookBase):
    pass


class BookOut(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)