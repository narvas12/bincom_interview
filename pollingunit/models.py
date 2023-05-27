from django.db import models

class State(models.Model):
    state_id = models.PositiveIntegerField(primary_key=True)
    state_name = models.CharField(max_length=255)

    def __str__(self):
        return self.state_name

class Lga(models.Model):
    lga_id = models.PositiveIntegerField(primary_key=True)
    lga_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.lga_name

class Ward(models.Model):
    ward_id = models.PositiveIntegerField(primary_key=True)
    ward_name = models.CharField(max_length=255)
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE)

    def __str__(self):
        return self.ward_name

class PollingUnit(models.Model):
    uniqueid = models.PositiveIntegerField(primary_key=True)
    polling_unit_id = models.PositiveIntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE)
    polling_unit_number = models.CharField(max_length=255)
    polling_unit_name = models.CharField(max_length=255)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    long = models.DecimalField(max_digits=11, decimal_places=8)
    entered_by_user = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    user_ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.polling_unit_name

class AnnouncedPuResults(models.Model):
    polling_unit_uniqueid = models.PositiveIntegerField()
    party_abbreviation = models.CharField(max_length=10)
    party_score = models.PositiveIntegerField()

    def __str__(self):
        return f"Polling Unit: {self.polling_unit_uniqueid}, Party: {self.party_abbreviation}"
