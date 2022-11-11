from django.shortcuts import render
import os
import mimetypes
import os
from django.http.response import HttpResponse
from .models import Potholedata
from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

def home(request):
    return render(request,'home.html')

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter, inch

def download_file(request):
    file_name = "simple_table.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    m = Potholedata.objects.get(id=1)
    data= [['Data',''],
        ['Address',m.Address ],
    ['Road_condition',m.Road_condition ],
    ['Killometers covered',m.kms_covered],
    ['Anomalies_detetcted',m.anomalies_detected],
    ['Pothole',m.pothole],
    ['Cracks',m.cracks],
    ['patches',m.patches]]
    t=Table(data)
    t=Table(data,2*[3.3*inch], 8*[0.5*inch],hAlign='LEFT')
    t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
    ('ALIGN',(0,0),(0,-1),'CENTER'),
    ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
    ('SPAN',(0,0),(-1,0)),
    ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
    ('TEXTCOLOR',(0,-1),(0,-1),colors.blue),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ]))
    elements.append(t)
    doc.build(elements)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    # Define the full file path
    filepath = os.path.join(BASE_DIR + '\simple_table.pdf')
    print(filepath)
    d = Drawing(800,800)
    pc = Pie()
    pc.x = 120
    pc.y = 300
    pc.height = 400
    pc.width = 400
    pc.data = [10,20,30]
    pc.labels = ['a','b','c']
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    # Return the response value
    return response

