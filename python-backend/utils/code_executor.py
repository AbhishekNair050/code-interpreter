import contextlib
import io


def execute_code(code):
    try:
        with contextlib.redirect_stdout(io.StringIO()) as f:
            exec(code, {})
            return f.getvalue()
    except Exception as e:
        print(f"Error executing code: {e}")
        return None
