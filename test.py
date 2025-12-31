from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://neondb_owner:npg_t4SjIhvYnWB5@ep-cool-rice-a13xxrmp-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
)

engine.connect()
print("Connected!")
