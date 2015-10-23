import bottle
from beaker.middleware import SessionMiddleware
from cork import Cork
import logging


logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)
bottle.debug(True)

# Use users.json and roles.json in the local example_conf directory
#starttls://username:password@smtp.gmail.com:587
aaa = Cork('/home/cwags/cwagswebforms/example_conf', email_sender='hdsheena@gmail.com', smtp_url='startttls://hdsheena@gmail.com:mysprintmydogsmylife@smtp.gmail.com:587')

# alias the authorization decorator with defaults
authorize = aaa.make_auth_decorator(fail_redirect="/login", role="user")

import datetime
app = bottle.app()
session_opts = {
    'session.cookie_expires': True,
    'session.encrypt_key': 'please use a random key and keep it secret!',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
}
app = SessionMiddleware(app, session_opts)


# #  Bottle methods  # #

def postd():
    return bottle.request.forms


def post_get(name, default=''):
    result = bottle.request.POST.get(name, default).strip()
    print result
    return result

@bottle.post('/login')
def login():
    """Authenticate users"""
    username = post_get('username')
    password = post_get('password')
    print username, password
    aaa.login(username, password, success_redirect='/', fail_redirect='/login')

@bottle.route('/user_is_anonymous')
def user_is_anonymous():
    if aaa.user_is_anonymous:
        return 'True'

    return 'False'

@bottle.route('/logout')
def logout():
    aaa.logout(success_redirect='/login')


@bottle.post('/register')
@bottle.view('/home/cwags/cwagswebforms/views/registration_email.tpl')
def register():
    """Send out registration email"""
    returned_output = aaa.register(post_get('username'), post_get('password'), post_get('email_address'))
    return str(returned_output)
    #return {}


@bottle.route('/validate_registration/:registration_code')
def validate_registration(registration_code):
    """Validate registration, create user account"""
    aaa.validate_registration(registration_code)
    return 'Thanks. <a href="/login">Go to login</a>'


@bottle.post('/reset_password')
def send_password_reset_email():
    """Send out password reset email"""
    aaa.send_password_reset_email(
        username=post_get('username'),
        email_addr=post_get('email_address')
    )
    return 'Please check your mailbox.'


@bottle.route('/change_password/:reset_code')
@bottle.view('password_change_form')
def change_password(reset_code):
    """Show password change form"""
    return dict(reset_code=reset_code)


@bottle.post('/change_password')
def change_password():
    """Change password"""
    aaa.reset_password(post_get('reset_code'), post_get('password'))
    return 'Thanks. <a href="/login">Go to login</a>'


@bottle.route('/')
@authorize()
def index():
    """Only authenticated users can see this"""
    #session = bottle.request.environ.get('beaker.session')
    #aaa.require(fail_redirect='/login')
    return 'Welcome! <a href="/admin">Admin page</a> <a href="/logout">Logout</a>'


# Resources used by tests designed to test decorators specifically

@bottle.route('/for_kings_only')
@authorize(role="king")
def page_for_kings():
    """
    This resource is used to test a non-existing role.
    Only kings or higher (e.g. gods) can see this
    """
    return 'Welcome! <a href="/admin">Admin page</a> <a href="/logout">Logout</a>'

@bottle.route('/page_for_specific_user_admin')
@authorize(username="admin")
def page_for_username_admin():
    """Only a user named 'admin' can see this"""
    return 'Welcome! <a href="/admin">Admin page</a> <a href="/logout">Logout</a>'

@bottle.route('/page_for_specific_user_fred_who_doesnt_exist')
@authorize(username="fred")
def page_for_user_fred():
    """Only authenticated users by the name of 'fred' can see this"""
    return 'Welcome! <a href="/admin">Admin page</a> <a href="/logout">Logout</a>'

@bottle.route('/page_for_admins')
@authorize(role="admin")
def page_for_role_admin():
    """Only authenticated users (role=user or role=admin) can see this"""
    return 'Welcome! <a href="/admin">Admin page</a> <a href="/logout">Logout</a>'



@bottle.route('/restricted_download')
@authorize()
def restricted_download():
    """Only authenticated users can download this file"""
    #aaa.require(fail_redirect='/login')
    return bottle.static_file('static_file', root='.')


@bottle.route('/my_role')
def show_current_user_role():
    """Show current user role"""
    session = bottle.request.environ.get('beaker.session')
    print "Session from simple_webapp", repr(session)
    aaa.require(fail_redirect='/login')
    return aaa.current_user.role


# Admin-only pages

@bottle.route('/admin')
@authorize(role="admin", fail_redirect='/sorry_page')
@bottle.view('admin_page')
def admin():
    """Only admin users can see this"""
    #aaa.require(role='admin', fail_redirect='/sorry_page')
    return dict(
        current_user = aaa.current_user,
        users = aaa.list_users(),
        roles = aaa.list_roles()
    )


@bottle.post('/create_user')
def create_user():
    try:
        aaa.create_user(postd().username, postd().role, postd().password)
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_user')
def delete_user():
    try:
        aaa.delete_user(post_get('username'))
        return dict(ok=True, msg='')
    except Exception, e:
        print repr(e)
        return dict(ok=False, msg=e.message)


@bottle.post('/create_role')
def create_role():
    try:
        aaa.create_role(post_get('role'), post_get('level'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_role')
def delete_role():
    try:
        aaa.delete_role(post_get('role'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


# Static pages

@bottle.route('/login')
@bottle.view('login_form')
def login_form():
    """Serve login form"""
    return {}


@bottle.route('/sorry_page')
def sorry_page():
    """Serve sorry page"""
    return '<p>Sorry, you are not authorized to perform this action</p>'


# #  Web application main  # #

def main():

    # Start the Bottle webapp
    bottle.debug(True)
    #bottle.run(app=app, quiet=False, reloader=True)
application = app
if __name__ == "__main__":
    main()