# === Stage 57: Add structured result objects for command handlers ===
# Project: ClientDesk
class CommandResult(BaseModel):
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    error_code: Optional[int] = None

def _build_success_result(data: Dict[str, Any], msg: str) -> CommandResult:
    return CommandResult(success=True, message=msg, data=data)

def _build_error_result(code: int, msg: str) -> CommandResult:
    return CommandResult(success=False, message=msg, error_code=code)
