let x = 1;
const URL = 'http://localhost:8080/api/';

function fetch() {
	$("#msgs").empty()
	$.get(URL + "entries/", function(data) {
		$("#entries").html(data);
	}).done(function() {
		$("#msgs").append('<div id="entries_msg" class="alert alert-success" role="alert">Liczba wpisów poprawnie załadowana.</div>');
	}).fail(function() {
		$("#msgs").append('<div id="entries_msg" class="alert alert-danger" role="alert">Nie udało się pobrać liczby wpisów.</div>');
	}).always(function() {
		setTimeout(function() {
		$("#entries_msg").hide('slow');
	}, 800);
	});
	
	$.get(URL + "users/", function(data) {
		$("#users").html(data.length);
		console.log(data);
	}).done(function() {
		$("#msgs").append('<div id="users_msg" class="alert alert-success" role="alert">Liczba użytkowników poprawnie załadowana.</div>');
	}).fail(function() {
		$("#msgs").append('<div id="users_msg" class="alert alert-danger" role="alert">Nie udało się pobrać liczby użytkowników.</div>');
	}).always(function() {
		setTimeout(function() {
		$("#users_msg").hide('slow');
	}, 1000);
	});

	$.get("http://localhost:8000/api/last_entry/", function(data) {
		$("#last_entry").html(data);
	}).done(function() {
		$("#msgs").append('<div id="last_entry_msg" class="alert alert-success" role="alert">Ostatni wpis poprawnie załadowany.</div>');
	}).fail(function() {
		$("#msgs").append('<div id="last_entry_msg" class="alert alert-danger" role="alert">Nie udało się pobrać ostatniego wpisu.</div>');
	}).always(function() {
		setTimeout(function() {
		$("#last_entry_msg").hide('slow');
	}, 1200);
	});
}

window.onload = function() {
	$.get(URL + "users/", function(data) {
		$("#users").html(data.length);
		console.log(data);
	}).done(function() {
		$("#msgs").append('<div id="users_msg" class="alert alert-success" role="alert">Liczba użytkowników poprawnie załadowana.</div>');
	}).fail(function() {
		$("#msgs").append('<div id="users_msg" class="alert alert-danger" role="alert">Nie udało się pobrać liczby użytkowników.</div>');
	}).always(function() {
		setTimeout(function() {
		$("#users_msg").hide('slow');
	}, 1000);
	});
	$("#user_form").submit(function(event) {

		$.post(URL + "users/", $("#user_form").serialize())
		.done(function() {
			//$("#msgs").append('<div id="user_add_msg" class="alert alert-primary" role="alert">Zarejestrowałeś się!</div>');
			alert('ok');
		}).fail(function() {
			$("#msgs").append('<div id="user_add_msg" class="alert alert-warning" role="alert">Rejestracja nie powiodła się.</div>');
		}).always(function(){
			fetch();
			$('#user_form').toggle();
		});
		return false;
	});
}