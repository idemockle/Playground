@call :abspath "%~0\..\floopyfloop"
@echo %_abspath_res%
@goto :eof

:abspath
@SET _abspath_res=%~f1
@goto :eof
