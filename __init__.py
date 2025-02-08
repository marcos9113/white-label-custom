from . import models
from . import controllers

MODULE = "_gamerun_whitelabel"


def uninstall_hook(env):
    env["ir.model.data"]._module_data_uninstall([MODULE])
