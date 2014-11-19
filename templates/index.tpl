{% extends "base.tpl" %}

{% block meta_title %}{% endblock %}
{% block title %}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

<div class="row">
	<div class="col-md-1 left"></div>
	<div class="col-md-10 middle">
	</div>
	<div class="col-md-1 right"></div>
</div>

{% endblock %}
