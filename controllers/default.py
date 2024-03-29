# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    form = crud.update(db.invoice, a0, next=URL('index'))
    facturi = db(db.invoice.created_by==auth.user.id).select(orderby=db.invoice.number)
    return locals()

@auth.requires_login()
def entries():
    f = db.invoice(a0)
    if f.created_by != auth.user.id:
        raise HTTP(500, 'Forbidden!') 
    db.entry.invoice.default = f
    form = crud.update(db.entry, a1)
    entries = db(db.entry.invoice == f.id).select()
    return locals()

@auth.requires_login()
def clients():
    form = crud.update(db.client, a0, next=URL('clients'))
    rows = db(db.client.created_by==auth.user.id).select(orderby=db.client.name)
    return response.render('default/firms.html', locals())

@auth.requires_login()
def firms():
    form = crud.update(db.firm, a0, next=URL('firms'))
    rows = db(db.firm.created_by==auth.user.id).select(orderby=db.firm.name)
    return locals()

def toggle_paid():
    f = db.invoice(a0)
    f.update_record(paid=not f.paid)
    redirect(URL('index'))

def show():
    f = db.invoice(a0)
    return locals()

def user():
    return dict(form=auth())


def download():
    return response.download(request,db)


def call():
    session.forget()
    return service()
