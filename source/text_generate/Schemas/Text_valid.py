from pydantic import BaseModel, Field, field_validator

class Text(BaseModel):
    text: str = Field(min_length=100, max_length=1700)
    
    #дополнительная валидация текста
    @field_validator('text')
    @classmethod
    def valid_text(cls, text):
        
        if '\n' in text or '\r' in text:
            raise ValueError ('текст содержит переносы строк')
        if ',' in text or '.' in text or ':' in text:
            raise ValueError ('текст содержит знаки препинания')
        
        return text
    