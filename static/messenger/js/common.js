$(document).ready(function() {

	$.post(
		'/chat/list', 
		{
		},
		function (data) {
			update_messages(data.messages);
			update_online_users(null);
		},
		'json'
	);

	$('#welcome-message').html("Welcome, "+$.cookie("username")+"!");
	
	$('#chat form').on('submit', function() {
		
		var message = $('#chat textarea[name=message]').val();

		if (message == '') {
			return false;
		};

		$('#chat textarea[name=message]').val('');
	
		clear_alert();
				
		var errors = Array();
		
		$.post(
			'/chat',
				{
				'message' : message
			},
			function (data) {
					$.post(
						'/chat/list', 
						{
						},
						function (data) {
							update_messages(data.messages);
						},
						'json'
					);
									
			},
			'json'
		);
		
		return false;
		
	});	
	

	$('#sign-in form').on('submit', function() {
		
		var login = $('#sign-in input[name=login]').val();
		var password = $('#sign-in input[name=password]').val();
	
		clear_alert();
				
		var errors = Array();
		
		$.post(
			'/auth/login',
				{
				'login' : login,
				'password' : password
			},
			function (data) {
				if (data.result == 'ok') {
					show_success(data.message);
				} else {
					errors.push(data.message);
					show_errors(errors);
				}
			},
			'json'
		);
		
		return false;
		
	});


	$('#registration form').on('submit', function() {
			
		var login = $('#registration input[name=login]').val();
		var email = $('#registration input[name=email]').val();
		var password = $('#registration input[name=password]').val();
		var password_repeat = $('#registration input[name=password-repeat]').val();
		
		var errors = Array();
		
		var login_check = check_login(login);
		var email_check = check_email(email);
		var password_check = check_password(password, password_repeat);
		
		if (login_check !== true) {
			errors.push(login_check);
		}
		
		if (email_check !== true) {
			errors.push(email_check);
		}
		
		if (password_check !== true) {
			errors.push(password_check);
		}
		
		if (errors.length > 0) {
			show_errors(errors);
			return false;
		} else {
			clear_alert();
		}
		
		$.post(
			'/auth/register',
			{
				'login' : login,
				'email' : email,
				'password' : password
			},
			function (data) {
				if (data.result == 'ok') {
					show_success(data.message);
				} else {
					errors.push(data.message);
					show_errors(errors);
				}
			},
			'json'
		);
		
		return false;
		
	});
});

function clear_alert() {
	$('.alert').removeClass('alert-error');
	$('.alert').removeClass('alert-success');
	$('.alert').hide();
	$('.alert').html('');
} 

function show_success(success) {
	$('.alert').addClass('alert-success');
	$('.alert').html(success);
	$('.alert').append('</ul>');
	$('.alert').show();
}

function show_errors(errors) {
	$('.alert').addClass('alert-error');
	$('.alert').html('');
	$('.alert').append('<ul>');
	for (i in errors) {
		$('.alert').append('<li>' + errors[i] + '</li>');
	}
	$('.alert').append('</ul>');
	$('.alert').show();
}

function check_login(val) {
	
	if (val == null || val.length == 0) {
		return 'Login is empty';
	}
	
	var pattern = /^[a-z0-9]+$/i;
	var result = pattern.test(val);
	if (result !== true) {
		return 'Login can only contains letters and numbers';
	}	
	
	return true;
	
}

function check_email(val) {
	
	if (val == null || val.length == 0) {
		return 'Email is empty';
	}
	
	var pattern = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;;
	var result = pattern.test(val);
	if (result !== true) {
		return 'Incorrect email format';
	}	
	
	return true;
	
}

function check_password(val, val_repeat) {
	
	if (val == null || val.length == 0) {
		return 'Password is empty';
	}
	
	if (val != val_repeat) {
		return 'Password does not match the confirm password';
	}
	
	return true;
}

function update_messages(data) {
	if (data ==null) {
		return false;
	};
	$('#messages').html('');
	var item;
	for (i in data) {
		item = '<div class="message" id="message-' + data[i][0] + '">' + ' ('+data[i][3]+') ' + data[i][1] +': ' + data[i][2] + '</div>';
		$('#messages').append(item);	
	}
}

function update_online_users(data) {
	if (data ==null) {
		return false;
	};
	$('#online-users').html('');
	$('#online-users').append("Online: "+data.length+" users");
	var item;
	for (i in data) {
		item = '<div class="message" id="message-' + data[i][0] + '">'+data[i][1]+'</div>';
		$('#online-users').append(item);	
	}
}