# backendpython
## Criar ambiente virtual
python -m venv venv

## Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate

## Ativar ambiente virtual (Windows)
venv\Scripts\activate

## Instalar FastAPI e servidor Uvicorn
pip install fastapi uvicorn[standard]

## Instalar ferramentas adicionais
pip install pydantic python-multipart python-jose[cryptography] passlib[bcrypt]


## # Backend
cd backend && npm run dev

# Frontend  
cd frontend && npm run dev

# Build para produção
cd frontend && npm run build
cd backend && npm run build