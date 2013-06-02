<!DOCTYPE html>
<html>
	<head>
		<title>Registration - Chat</title>
		<meta charset="utf-8" />
		<link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">
		<link href="/static/messenger/css/common.css" rel="stylesheet">
		<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="/static/jquery/js/jquery-1.9.1.min.js"></script>
		<script type="text/javascript" src="/static/messenger/js/common.js"></script>
	</head>
	<body>
		<div id="wrap">		
			<div id="registration">			
				<form method="post" action="/auth/register">
					<h1>Registration</h1>
					Login:<br /><input type="text" name="login"/><br />
					Email:<br /><input type="text" name="email"/><br />
					Password:<br /><input type="password" name="password"/><br />
					Repeat Password:<br /><input type="password" name="password-repeat"/><br />
					<input type="submit" value="Register" class="btn" />
				</form>
				<div class="alert hide"></div>
			</div>
		</div>
	</body>
</html>