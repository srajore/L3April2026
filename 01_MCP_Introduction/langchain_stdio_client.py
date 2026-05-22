import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

PYTHON_EXE="D:\\L3April2026\\.venv\\Scripts\\python.exe"
MCP_SERVER_SCRIPT='D:\\L3April2026\\01_MCP_Introduction\\stdio_server.py'


async def main():
    client = MultiServerMCPClient({
        "data_fetch_mcp_stdio": {
            "transport": "stdio",
            "command": PYTHON_EXE,
            "args": [MCP_SERVER_SCRIPT]
        }
    })
    
    
    # fetch and dispaly available tools
    
    tools= await client.get_tools()
    
    print("Available tools:", tools)
    
    
if __name__ == "__main__":
    asyncio.run(main())
    
    
    



