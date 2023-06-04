from construct import db, login_manager
from construct import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#MODEL FOR USER STORAGE
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    password_hash = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    role = db.Column(db.String(length=30), nullable=False, unique=False)
    contact_number = db.Column(db.String(length=30), nullable=False, unique=False)
   
     
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_pwd):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_pwd).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)



#FOR MIR,WIR,DELAYS USE THE BELOW NAMING CONVENTION FOR STATUS TYPES
#Use the following status types in forms: Submitted,Approved, Approved-As-Noted, Revise-and-ReSubmit, Rejected


#ALL MODALS FOR DELAYS AND EOT STORAGE

class EOTDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    eot_file_name = db.Column(db.String(length=30), nullable=False)
    eot_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)

class EOTConsultantDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    eot_file_name = db.Column(db.String(length=30), nullable=False)
    eot_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)

class Delay(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    type = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=30), nullable=False)
    severity = db.Column(db.String(length=30), nullable=False)
    phase = db.Column(db.String(length=30), nullable=True,default="Default")
    delayed_days = db.Column(db.Integer(), nullable=True)
    date = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=True, default="Submitted")


#ALL MODELS FOR TASK MANAGEMENT
class Tasks(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    Name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=30), nullable=False)
    phase = db.Column(db.String(length=30), nullable=False)
    Percentage = db.Column(db.Integer(), nullable=False,default=0)
    start_date = db.Column(db.String(length=30), nullable=False)
    end_date = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=True, default="Pending")
    total_estimated_cost = db.Column(db.String(length=30), nullable=False)
    total_days = db.Column(db.Integer(), nullable=False)
  

class TaskToImage(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    img_name = db.Column(db.String(length=30), nullable=False)
    task_id = db.Column(db.String(length=30), nullable=False)
    uploaded_date = db.Column(db.String(length=30), nullable=False)



#ALL MODELS FOR WORK INSPECTION REQUESTS
class WorkInspectionRequests(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    type = db.Column(db.String(length=30), nullable=False)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=True, default="Submitted")
    submitted_date = db.Column(db.String(length=30), nullable=False)

class WIRDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    wir_file_name = db.Column(db.String(length=30), nullable=False)
    wir_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)
    
class WIRConsultantDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    wir_file_name = db.Column(db.String(length=30), nullable=False)
    wir_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)


#ALL MODELS FOR MATERIAL INSPECTION REQUESTS
class MaterialInspectionRequests(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    type = db.Column(db.String(length=30), nullable=False)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=True, default="Submitted")
    submitted_date = db.Column(db.String(length=30), nullable=False)

class MIRDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    mir_file_name = db.Column(db.String(length=30), nullable=False)
    mir_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)
class MIRConsultantDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    mir_file_name = db.Column(db.String(length=30), nullable=False)
    mir_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)


#ALL MODELS FOR MATERIAL INSPECTION REQUESTS
class VariationInspectionRequests(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=True, default="Submitted")
    submitted_date = db.Column(db.String(length=30), nullable=False)

class VariationDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    variation_file_name = db.Column(db.String(length=30), nullable=False)
    variation_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)
class VariationConsultantDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    variation_file_name = db.Column(db.String(length=30), nullable=False)
    variation_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)


#ALL MODELS FOR Payment requests
class PaymentRequests(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=True, default="Submitted")
    submitted_date = db.Column(db.String(length=30), nullable=False)
    type=  db.Column(db.String(length=30), nullable=False)

class PaymentDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    payment_file_name = db.Column(db.String(length=30), nullable=False)
    payment_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)
class PaymentConsultantDocument(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    payment_file_name = db.Column(db.String(length=30), nullable=False)
    payment_id = db.Column(db.String(length=30), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
    submitted_date = db.Column(db.String(length=30), nullable=False)
    submitted_by=db.Column(db.String(length=30), nullable=False)



    
