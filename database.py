from sqlmodel import Session, create_engine

DATABASE_URL = "postgresql://minhdangpy134:minhdang@localhost:5432/vnmark"
engine = create_engine(DATABASE_URL, echo=True)

# Không cần sessionmaker
def get_db():
    with Session(engine) as session:
        yield session
