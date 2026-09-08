from mcp.server.mcpserver import MCPServer

mcp = MCPServer("grettings")

@mcp.tool()
def greet(name: str) -> str:
    """
    Greet the user with a personalized message.
    """
    return f"Hello, {name}! Welcome to our service."

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
    )