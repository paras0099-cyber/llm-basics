# LLM Basics with LangChain & Google Gemini

> **Today I learned LangChain & LLM fundamentals:** Exploring chat models, multi-role chat messages, reusable prompt templates, LCEL pipe operators, and structured outputs using Google Gemini and Pydantic.

---

## 📚 What I Learned Today

### 1. Simple LLM Invocation ([`hello-llm.py`](hello-llm.py))
- Setting up `ChatGoogleGenerativeAI` with Google Gemini (`gemini-1.5-flash`).
- Basic invocation with standard text prompts and printing the response content.

### 2. Multi-Role Chat Messages ([`chat_messages.py`](chat_messages.py))
- Crafting structured conversations using `SystemMessage` (role/instructions) and `HumanMessage` (user inquiry).
- Guiding model responses through system prompt personas.

### 3. Prompt Templates ([`prompt_templates.py`](prompt_templates.py))
- Creating dynamic prompts using `ChatPromptTemplate.from_messages(...)`.
- Injecting variables (`{profession}`, `{question}`) into the prompt using `.invoke({...})`.

### 4. LCEL & Pipe Operators ([`pipe_operatores.py`](pipe_operatores.py))
- Building LangChain Expression Language (LCEL) chains with the `|` pipe operator.
- Connecting components: `prompt_template | llm | StrOutputParser()`.
- Automatically parsing responses directly into plain strings.

### 5. Structured Outputs ([`structured_outputs.py`](structured_outputs.py))
- Enforcing structured schema responses using Pydantic `BaseModel` and `.with_structured_output(...)`.
- Generating structured quiz items with options, correct answer indices, and explanations.

---

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/paras0099-cyber/llm-basics.git
cd llm-basics
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file in the root folder:
```env
GOOGLE_API_KEY="your-google-api-key"
```

### 4. Run the examples
```bash
python hello-llm.py
python chat_messages.py
python prompt_templates.py
python pipe_operatores.py
python structured_outputs.py
```
