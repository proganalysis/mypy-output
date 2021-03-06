from impacts_world.contrib.forms import HeadingAbstractFormField
from typing import Any, Optional
from wagtail.contrib.settings.models import BaseSetting
from wagtail.wagtailcore.models import Page
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormSubmission

class HomePage(Page):
    landing_page_template: str = ...
    parent_page_types: Any = ...
    content: Any = ...
    content_panels: Any = ...

class SidebarPage(Page):
    intro: Any = ...
    parent_page_types: Any = ...
    content: Any = ...
    content_panels: Any = ...
    def get_context(self, request: Any, *args: Any, **kwargs: Any): ...

class GenericPage(Page):
    template: str = ...
    content: Any = ...
    content_panels: Any = ...

class FormField(HeadingAbstractFormField):
    page: Any = ...

class FormPage(AbstractEmailForm):
    form_builder: Any = ...
    landing_page_template: str = ...
    subpage_types: Any = ...
    timeline_snippet: Any = ...
    intro: Any = ...
    content: Any = ...
    confirmation_text: Any = ...
    send_confirmation_email: Any = ...
    confirmation_email_subject: Any = ...
    confirmation_email_text: Any = ...
    form_title: Any = ...
    button_name: Any = ...
    content_panels: Any = ...
    def get_context(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_data_fields(self): ...
    def get_submission_class(self): ...
    def serve(self, request: Any, *args: Any, **kwargs: Any): ...
    def process_form_submission(self, form: Any) -> None: ...

class CustomFormSubmission(AbstractFormSubmission):
    identifier: Any = ...
    def get_data(self): ...

TIMELINE_ITEM_PLENARY: str
TIMELINE_ITEM_WORKSHOP: str
TIMELINE_ITEM_POSTER: str
TIMELINE_ITEM_SPECIAL: str
TIMELINE_ITEM_TYPES: Any

class ProgramOverviewPage(Page):
    parent_page_types: Any = ...
    subpage_types: Any = ...
    intro: Any = ...
    content: Any = ...
    content_panels: Any = ...
    def get_sidebar_menu(self, active_menu_item: Optional[Any] = ...): ...
    def get_context(self, request: Any, *args: Any, **kwargs: Any): ...

class ProgrammeItemPage(Page):
    description: Any = ...
    date_time: Any = ...
    room: Any = ...
    icon: Any = ...
    parent_page_types: Any = ...
    content_panels: Any = ...
    class Meta:
        abstract: bool = ...

class PlenaryItemPage(ProgrammeItemPage):
    content: Any = ...
    content_panels: Any = ...
    def get_keynotes(self): ...

class WorkshopItemPage(ProgrammeItemPage):
    convenor_name: Any = ...
    convenor_institute: Any = ...
    content: Any = ...
    content_panels: Any = ...

class PosterItemPage(ProgrammeItemPage):
    content: Any = ...
    content_panels: Any = ...

class AbstractOverviewPage(Page):
    intro: Any = ...
    parent_page_types: Any = ...
    content_panels: Any = ...
    class Meta:
        abstract: bool = ...

class PlenaryOverviewPage(AbstractOverviewPage):
    subpage_types: Any = ...
    template: str = ...
    def get_context(self, request: Any, *args: Any, **kwargs: Any): ...

class WorkshopOverviewPage(AbstractOverviewPage):
    subpage_types: Any = ...
    template: str = ...
    def get_workshops(self, date_time: Any): ...
    def get_context(self, request: Any, *args: Any, **kwargs: Any): ...

class WorkshopChallengePage(Page):
    description: Any = ...
    challenge_icon: Any = ...
    workshop_icon: Any = ...
    content_panels: Any = ...
    parent_page_types: Any = ...
    subpage_types: Any = ...

class PosterOverviewPage(AbstractOverviewPage):
    subpage_types: Any = ...
    template: str = ...
    def get_context(self, request: Any, *args: Any, **kwargs: Any): ...

class FooterSettings(BaseSetting):
    content: Any = ...
    panels: Any = ...
