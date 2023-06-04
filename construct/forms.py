from construct import FlaskForm
from construct import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from construct.models import User
from wtforms import IntegerField, DateField, SelectField

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('The username is taken already')

    def validate_email_address(self, email_to_check):
        email_add = User.query.filter_by(
            email_address=email_to_check.data).first()
        if email_add:
            raise ValidationError(
                'The email address is taken already')

    username = StringField(label='User Name', validators=[
                           Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[
                                Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[
                              Length(min=6), DataRequired()])
    password2 = PasswordField(label='Password Confirmation', validators=[
                              EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account!')
    role = SelectField(u'Select User Role', choices=[('Client', 'Client'), ('Consultant', 'Consultant'), ('Contractor', 'Contractor')])
    contact_no= StringField(label='Contact Number', validators=[DataRequired(),Length(max=12),Length(min=12)])

 #--------------------------------------------------------------------
class UserEditForm(FlaskForm):



    
    email_address = StringField(label='Email Address', validators=[
                                Email()])
    password1 = PasswordField(label='Password', validators=[
                              Length(min=6)])
    password2 = PasswordField(label='Password Confirmation', validators=[
                              EqualTo('password1')])
    submit = SubmitField(label='Submit Changes')
    role = SelectField(u'Select User Role', choices=[('Client', 'Client'), ('Consultant', 'Consultant'), ('Contractor', 'Contractor')])
    contact_no= StringField(label='Contact Number',validators=[Length(max=12),Length(min=12)])
#--------------------------------------------------------------------
class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    login_password = StringField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

#--------------------------------------------------------------------
class DelayForm(FlaskForm):

    type_of = SelectField(u'Category', choices=[('Workforce', 'Workforce'), ('Financial', 'Financial'), ('Weather', 'Weather'), ('Logistics', 'Logistics'), (' Miscellaneous', ' Miscellaneous')])
    description = StringField(label='Description', validators=[
                                DataRequired()])

    severity = SelectField(u'Severity', choices=[('Minor', 'Minor'), ('Medium', 'Medium'), ('Major', 'Major')])
    phase = SelectField(u'Phase', choices=[('Foundation', 'Foundation'), ('Interior', 'Interior'), ('Electrical', 'Electrical'), ('Plumbing', 'Plumbing'), ('Safety', 'Safety')])
    extended_days = IntegerField(label='Request for EOT in Days', validators=[
                             DataRequired()])
    date = DateField('Date', format='%Y-%m-%d') 
    submit = SubmitField(label='Submit Delay!')

#--------------------------------------------------------------------
class TaskForm(FlaskForm):
    Name = StringField(label='Name', validators=[
                                DataRequired()])
    Description = StringField(label='Description', validators=[
                                DataRequired()])

    phase = SelectField(u'Type', choices=[('Foundation', 'Foundation'), ('Interior', 'Interior'), ('Electrical', 'Electrical'), ('Plumbing', 'Plumbing'), ('Safety', 'Safety'),('Roofing', 'Roofing'),('Exterior', 'Exterior'),('Paint', 'Paint')])
    

    start_date = DateField('Start Date', format='%Y-%m-%d') 
    end_date = DateField('End Date', format='%Y-%m-%d') 

    total_estimated_cost = IntegerField(label='Total estimated cost', validators=[
                             DataRequired()])

    submit = SubmitField(label='Submit Task')
    #Function to check if start date is greater than end date
    def validate_on_submit(self):
            
            if (self.start_date.data>self.end_date.data):
                return False
            else:
                return True
    
#--------------------------------------------------------------------

class WIRSubmitForm(FlaskForm):
    Name = StringField(label='Name', validators=[
                                DataRequired()])
    
    Description = StringField(label='Description', validators=[
                                DataRequired()])
    Type = SelectField(u'Type', choices=[('Plumbing', 'Plumbing'), ('Electrical', 'Electrical'), ('Roofing', 'Roofing'),('Flooring', 'Flooring'),('Interior', 'Interior')])
    submit = SubmitField(label='Submit WIR')
#--------------------------------------------------------------------
class MIRSubmitForm(FlaskForm):
    Name = StringField(label='Name', validators=[
                                DataRequired()])
    Description = StringField(label='Description', validators=[
                                DataRequired()])
    Type = SelectField(u'Type', choices=[('Raw Material', 'Raw Material'), ('Electrical', 'Electrical'), ('Roofing', 'Roofing'),('Metal', 'Metal'),('Interior', 'Interior')])
    submit = SubmitField(label='Submit MIR')
#--------------------------------------------------------------------
class VariationSubmitForm(FlaskForm):
    Name = StringField(label='Name', validators=[
                                DataRequired()])
    Description = StringField(label='Description', validators=[
                                DataRequired()])
    
    submit = SubmitField(label='Submit Variation Request')
#--------------------------------------------------------------------
class PaymentSubmitForm(FlaskForm):
    Name = StringField(label='Name', validators=[
                                DataRequired()])
    Description = StringField(label='Description', validators=[
                                DataRequired()])
    Type = SelectField(u'Type', choices=[('Interim-Payment', 'Interim-Payment'), ('On-Account Payment', 'On-Account Payment'), ('Final Payment', 'Final Payment')])
    
    submit = SubmitField(label='Submit Payment Request')
#--------------------------------------------------
class TaskPercentageForm(FlaskForm):
    percentage_completed = IntegerField(label='Percentage Completed', validators=[
                             DataRequired()])
    
    submit = SubmitField(label='Submit Task Update')
 