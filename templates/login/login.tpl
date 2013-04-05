<!DOCTYPE html>
<html>
	<head>
		<title>Chat</title>
		<meta charset="utf-8" />
		<link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">
		<link href="/static/messenger/css/common.css" rel="stylesheet">
		<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="/static/jquery/js/jquery-1.9.1.min.js"></script>
	</head>
	<body>
		<div id="wrap">		
		
			<div id="auth-block">			
				<form method="post" action="/auth/login">
					Authentication:<br />
					Login:<input type="text" name="login"/><br />
					Password:<input type="text" name="password"/><br />
					<input type="submit" value="Log In" class="btn" />
				</form>
				<form method="post" action="/auth/register">
					Registration:<br />
					Login:<input type="text" name="login"/><br />
					Password:<input type="text" name="password"/><br />
					<input type="submit" value="Register" class="btn" />
				</form>
			</div>
		</div>
	</body>
</html>