import os
import json
from openai import OpenAI

# 1. Konfigurasi Client DeepSeek
# Pastikan Anda sudah mengatur environment variable DEEPSEEK_API_KEY
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"), 
    base_url="https://api.deepseek.com"
)

# 2. Definisikan Tools (Function Calling)
# Kami mendefinisikan skema fungsi yang bisa dipanggil oleh model
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Mendapatkan harga saham terbaru dari simbol tertentu",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Simbol saham (misal: AAPL, TSLA, BBCA.JK)",
                    },
                },
                "required": ["symbol"],
            },
        },
    }
]

# Fungsi simulasi untuk mengambil data saham
def get_stock_price(symbol):
    print(f"\n[Sistem] Memanggil Tool: get_stock_price('{symbol}')")
    # Data simulasi
    stock_data = {
        "AAPL": "190.50 USD",
        "TSLA": "175.20 USD",
        "BBCA.JK": "10,125 IDR"
    }
    price = stock_data.get(symbol.upper(), "Data tidak ditemukan")
    return json.dumps({"symbol": symbol, "price": price})

def run_deepseek_tool_example():
    print("--- DeepSeek Tool Use Example ---")
    
    messages = [
        {"role": "system", "content": "You are a specialized financial assistant."},
        {"role": "user", "content": "Berapa harga saham Apple (AAPL) hari ini?"}
    ]

    print(f"User: {messages[1]['content']}")

    # 3. Kirim ke DeepSeek dengan definisi tools
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # 4. Tangani Tool Calls jika ada
    if tool_calls:
        messages.append(response_message) # Tambahkan pesan asisten ke history

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            if function_name == "get_stock_price":
                # Eksekusi fungsi di sisi client
                result = get_stock_price(symbol=function_args.get("symbol"))
                
                # Kirim hasil kembali ke AI
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": result,
                })
        
        # 5. Dapatkan respon akhir dari AI setelah menerima data tool
        final_response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        print(f"AI: {final_response.choices[0].message.content}")
    else:
        print(f"AI: {response_message.content}")

if __name__ == "__main__":
    run_deepseek_tool_example()
