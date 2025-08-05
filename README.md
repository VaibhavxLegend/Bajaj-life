# Bajaj-life
Team Bajaj

llm_query_system/
├── app/
│   ├── main.py                 # FastAPI startup
│   ├── config.py               # Settings & secrets
│   ├── api/
│   │   └── routes.py           # /hackrx/run endpoint
│   ├── models/
│   │   └── schema.py           # Pydantic request/response models
│   ├── services/
│   │   ├── document_loader.py  # PDF/DOCX/email → text
│   │   ├── embeddings.py       # chunk/embed/upsert & query
│   │   ├── query_parser.py     # NL → structured query
│   │   ├── clause_matcher.py   # retrieval + LLM ranking/explanation
│   │   ├── logic_processor.py  # domain logic extraction
│   │   └── formatter.py        # build JSON payload
│   ├── utils/
│   │   └── helpers.py          # misc utilities
│   └── db/
│       ├── base.py             # SQLAlchemy base
│       ├── models.py           # Document/Query/Response tables
│       └── session.py          # DB session factory
├── tests/                      # pytest suites
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
