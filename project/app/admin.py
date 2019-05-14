from django.contrib import admin
from app.models import Location, Cinema, Movie, Review, FilmManager, Ticket


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact',
                    'avg_cost', 'section', 'image_url',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cinema',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'dish_name', 'count', 'user',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'restaurant',)
