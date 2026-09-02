from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg://fangst:fangst@localhost:5432/fangstplot")