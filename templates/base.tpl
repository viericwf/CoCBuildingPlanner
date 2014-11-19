<!doctype html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="title" content="{% block meta_title %}{% endblock %}">
    <meta name="keywords" content="{% block meta_keywords %}{% endblock %}">
    <meta name="description" content="{% block meta_description %}{% endblock %}">
    <title>CoC Building Planner</title>

    <link rel="shortcut icon" href="{{ url_for('static', filename='img/favicon.ico') }}">

    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap-theme.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/font-awesome.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/shared.css') }}">

    {% block extra_css %}
    {% endblock %}

    <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap-extras.js') }}"></script>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>


    {% block extra_js %}
    {% endblock %}

    <!--[if lt IE 9]>
    <script src="{{ url_for('static', filename='js/html5shiv.js') }}"></script>
    <script src="{{ url_for('static', filename='js/respond.min.js') }}"></script>
    <![endif]-->

    {% block extra_head %}
    {% endblock %}

</head>

<body>
<div id="navbar-top" class="navbar navbar-fixed-top" role="navigation">
    <div class="navbar-header">CoC Building Planner</div>
</div>


<!-- main block -->
<div class="container main-block-wrap">
    {% block main %}
    {% endblock %}
</div>

</body>
</html>
