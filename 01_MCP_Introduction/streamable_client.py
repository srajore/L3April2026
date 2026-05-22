import asyncio
from fastmcp import Client


async def main():
    client = Client("http://127.0.0.1:8000/mcp")
    
    async with client:
        tools = await client.list_tools()  # List available tools
        
        print("Available tools:", tools)
        
        result = await client.call_tool(
            "add",
            {"a": 7, "b": 3}
        )
    
        print("Result:", result)
        
        
        
if __name__ == "__main__":
    asyncio.run(main())