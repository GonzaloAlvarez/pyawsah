"""Console script for pyawsah."""
import sys
import click
from loguru import logger
from click_loguru import ClickLoguru
from .awsah import list_profiles, list_roles, show_account_info, show_account_url, create_role

__program__ = 'awsah'
__version__ = '0.0.1'

log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"
click_loguru = ClickLoguru(__program__, __version__, stderr_format_func=lambda x: log_format)


@click.group()
@click_loguru.logging_options
@click_loguru.stash_subcommand()
@click.version_option(prog_name=__program__, version=__version__)
@click.pass_context
def main(ctx, **kwargs):
    pass


@main.command(name='profiles', help='list profiles')
@click_loguru.init_logger(logfile=False)
@click.pass_context
def profiles(ctx, **kwargs):
    list_profiles()

@main.command(name='roles', help='list roles')
@click_loguru.init_logger(logfile=False)
@click.option("--profile", required=True, help="Specify the profile to use")
def roles(profile):
    """List all console roles"""
    list_roles(profile)

@main.command(help="Show account info")
@click_loguru.init_logger(logfile=False)
@click.option("--profile", required=True, help="Specify the profile to use")
def info(profile):
    """Show account info"""
    show_account_info(profile)

@main.command(help="Create new role")
@click_loguru.init_logger(logfile=False)
@click.option("--profile", required=True, help="Specify the profile to use")
@click.option("--name", required=True, help="Specify the name of the role")
def newrole(profile, name):
    create_role(profile, name)


@main.command(help="Show account url for federated login")
@click_loguru.init_logger(logfile=False)
@click.option("--profile", required=True, help="Specify the profile to use")
@click.option("--role", required=True, help="Specify the role to use")
def url(profile, role):
    show_account_url(profile, role)
