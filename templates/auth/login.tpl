<!DOCTYPE html>
<html>
	<head>
		<title>Login - Chat</title>
		<meta charset="utf-8" />
		<link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">
		<link href="/static/messenger/css/common.css" rel="stylesheet">
		<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="/static/jquery/js/jquery-1.9.1.min.js"></script>
		<script type="text/javascript" src="/static/messenger/js/common.js"></script>
	</head>
	<body>
		<div id="wrap">		
			<div id="sign-in">			
				<form method="post" action="/auth/login">
					<h1>Sign in</h1>
					Login:<br /><input type="text" name="login"/><br />
					Password:<br /><input type="password" name="password"/><br />
					<input type="submit" value="Login" class="btn" />
				</form>
				<div class="alert hide"></div>
				<div class="help">
					<ul>
						<li><a href="/auth/register">Register</a></li>
					</ul>
				</div>
			</div>
		</div>
	</body>
</html>