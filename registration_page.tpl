
%from bottle import template
%passedIntoTpl = rows
<html>
<body>
<h1>Register to use online sign up</h1>
%form = template('make_form',  rows=passedIntoTpl, action=("/register"))

{{!form}}
</body>
</html>
