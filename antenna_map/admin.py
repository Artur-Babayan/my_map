# from django.contrib import admin
# from .models import Antenna
#
#
# admin.site.register(Antenna)


from django.contrib import admin
from .models import Antenna
import csv
from io import TextIOWrapper

class AntennaAdmin(admin.ModelAdmin):
    actions = ['import_csv']

    def import_csv(self, request, queryset):
        file = request.FILES.get('csv_file')
        if not file.name.endswith('.csv'):
            self.message_user(request, 'File is not a CSV file')
            return
        reader = csv.reader(TextIOWrapper(file.file, encoding='utf-8'))
        for row in reader:
            name = row[0]
            configuration = row[1]
            latitude = float(row[2].replace(',', '.'))
            longitude = float(row[3].replace(',', '.'))
            Antenna.objects.create(name=name, configuration=configuration, latitude=latitude, longitude=longitude)
        change_list_template = 'admin/antenna_change_list.html'

        self.message_user(request, 'CSV file imported successfully')

admin.site.register(Antenna, AntennaAdmin)
