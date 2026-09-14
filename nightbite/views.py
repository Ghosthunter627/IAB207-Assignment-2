from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/event')
def event():
    return render_template('event.html')


@main_bp.route('/create-event')
def create_event():
    return render_template('create-event.html')


@main_bp.route('/bookings')
def bookings():
    return render_template('bookings.html')