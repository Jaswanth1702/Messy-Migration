from marshmallow import Schema, fields, validate, ValidationError

def validate_email(email):
    if '@' not in email:
        raise ValidationError('Invalid email address.')

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True, validate=validate_email)
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
