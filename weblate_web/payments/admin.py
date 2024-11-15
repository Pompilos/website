#
# Copyright © Michal Čihař <michal@weblate.org>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from django.contrib import admin

from .models import Customer, Payment


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "country", "vat", "origin")
    list_filter = ("country", "origin")
    search_fields = ("name", "email")


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "amount",
        "customer",
        "state",
        "backend",
        "repeat",
        "start",
        "end",
        "invoice",
    )
    list_filter = ("state", "backend", "customer__name", "customer__origin")
    search_fields = (
        "description",
        "customer__name",
        "customer__email",
        "invoice",
        "draft_invoice__number",
        "paid_invoice__number",
    )
    readonly_fields = ("created",)
    date_hierarchy = "created"


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)
