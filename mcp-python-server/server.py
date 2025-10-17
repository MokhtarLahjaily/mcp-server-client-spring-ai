from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

mcp = FastMCP('Python MCP Server')

@mcp.tool()
def get_info_about(name: str) -> Dict[str, Any]:
    """
    Get Information about a given employee name:
    - Employee Name
    - Salary
    """
    return {
        "employee_name": "Mokhtar",
        "salary": 5400,
    }

if __name__ == "__main__":
    mcp.run()
