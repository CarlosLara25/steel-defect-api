from pydantic import BaseModel, Field
from datetime import datetime


class PredictionRequest(BaseModel):
    X_Minimum: int = Field(ge=0)
    X_Maximum: int = Field(ge=0)
    Y_Minimum: int = Field(ge=0)
    Y_Maximum: int = Field(ge=0)
    Pixels_Areas: int = Field(ge=0)
    X_Perimeter: int = Field(ge=0)
    Y_Perimeter: int = Field(ge=0)
    Sum_of_Luminosity: int = Field(ge=0)
    Minimum_of_Luminosity: int = Field(ge=0)
    Maximum_of_Luminosity: int = Field(ge=0)
    Length_of_Conveyer: int = Field(ge=0)

    TypeOfSteel_A300: bool
    TypeOfSteel_A400: bool

    Steel_Plate_Thickness: int = Field(ge=0)

    Edges_Index: float = Field(ge=0, le=1)
    Empty_Index: float = Field(ge=0, le=1)
    Square_Index: float = Field(ge=0, le=1)
    Outside_X_Index: float = Field(ge=0, le=1)
    Edges_X_Index: float = Field(ge=0, le=1)
    Edges_Y_Index: float = Field(ge=0, le=1)
    Outside_Global_Index: float = Field(ge=0, le=1)

    LogOfAreas: float
    Log_X_Index: float
    Log_Y_Index: float

    Orientation_Index: float = Field(ge=-1, le=1)
    Luminosity_Index: float = Field(ge=-1, le=1)
    SigmoidOfAreas: float = Field(ge=0, le=1)


class ResponseSchema(BaseModel):
        request_id: str
        prediction: str
        confidence: float = Field(ge=0, le=1)
        model_version: str
        timestamp: datetime
        