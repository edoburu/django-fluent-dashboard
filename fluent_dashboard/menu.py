"""
Custom menu for fluent_dashboard apps.
"""
from django.utils.translation import gettext_lazy as _

from admin_tools.menu import Menu, items
from admin_tools.utils import get_admin_site_name
from django.urls import reverse
from fluent_dashboard.appgroups import get_application_groups
from fluent_dashboard.items import CmsModelList, ReturnToSiteItem


class FluentMenu(Menu):
    """
    Custom Menu for admin site.

    The top level menu items created by this menu reflect the application groups
    defined in :ref:`FLUENT_DASHBOARD_APP_GROUPS`. By using both
    the :class:`~fluent_dashboard.dashboard.FluentIndexDashboard` and this class,
    the menu and dashboard modules at the admin index page will consistent.
    The :class:`~fluent_dashboard.items.ReturnToSiteItem` is also added at the end of the menu.

    To activate the menu add the following to your settings.py::

        ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'
    """

    def init_with_context(self, context):
        """
        Initialize the menu items.
        """
        site_name = get_admin_site_name(context)

        self.children += [
            items.MenuItem(_("Dashboard"), reverse(f"{site_name}:index")),
            items.Bookmarks(),
        ]

        for title, kwargs in get_application_groups():
            if kwargs.get("enabled", True):
                self.children.append(CmsModelList(title, **kwargs))

        self.children += [ReturnToSiteItem()]
