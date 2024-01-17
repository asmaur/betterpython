"""Exemplo de como ler e validar dados com pydantic"""

import json
import pydantic
from typing import Optional, List

class ISBN10FormatError(Exception):
    """Exception a ser emitida quando o formato de ISBN10 estiver errado."""
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class ISBNMissingError(Exception):
    """ISBN10 ou ISBN13 estão ausentes"""
    def __init__(self, title: str, message: str) -> None:
        self.message = message
        self.title = title
        super().__init__(message)

class Livro(pydantic.BaseModel):
    title: str    
    author: str
    price: float
    publisher: str
    isbn_10: Optional[str] = None
    isbn_13: Optional[str] = None
    subtitle: Optional[str] = None
    
    @pydantic.model_validator(mode="before")
    @classmethod
    def verificar_isbn10_ou_isbn13(cls, values):
        """Verificar a existência do isbn10 ou isbn13."""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Um livro deve ter pelo menos ISBN10 ou ISBN13."
            )
        return values

    @pydantic.field_validator("isbn_10")
    @classmethod
    def validar_isbn_10(cls, value):
        """Validar o código ISBN10."""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(vale=value, message="O código ISBN10 precisa ter 10 digitos.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        
        soma_esperado = sum((10-i) * char_to_int(x) for i , x in enumerate(chars))
        if soma_esperado % 11 !=0 :
            raise ISBN10FormatError(vale=value, message="A soma dos digitos do código ISBN10 deve ser divisível por 11.") 
        return value

    class Config:
        """Classe de configuração."""
        frozen = True

def main() -> None:
    with open("pydantic/data.json") as file:
        data = json.load(file)
        livros: List[Livro] = [Livro(**item) for item in data]
        print(livros[2].title)


if __name__ == "__main__":
    main()