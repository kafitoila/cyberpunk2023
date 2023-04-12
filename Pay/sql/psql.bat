@echo off
setlocal
chcp 1251
if [%1]==[] (set psqlhost=localhost) else (set psqlhost=%1)
if [%2]==[] (set psqluser=postgres) else (set psqluser=%2)
if [%3]==[] (set psqldbase=postgres) else (set psqldbase=%3)
if [%4]==[] (set psqlport=5432) else (set psqlport=%4)

"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PostgreSQL 15\psql.exe" -h %psqlhost% -U %psqluser% -d %psqldbase% -p %psqlport%
endlocal