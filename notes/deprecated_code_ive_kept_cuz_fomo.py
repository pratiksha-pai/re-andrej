    def get_variable_name(self):
        import inspect
        frame = inspect.currentframe()
        try:
            outer_frame = frame.f_back
            var_name = [name for name, value in outer_frame.f_locals.items() if value is self]
            return_val = var_name[0] if var_name else None
            print("returning from get_variable_name = ", return_val)
            return return_val
        finally:
            del frame