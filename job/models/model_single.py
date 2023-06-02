import uuid

from clickhouse_backend import models


class Job(models.ClickhouseModel):
    class Meta:
        verbose_name = 'Jobs'
        db_table = 'jobdarjob_single'
        ordering = ['-publication_date']
        engine = models.ReplacingMergeTree(
            order_by=['publication_date'],
        )

    id = models.UUIDField(unique=True, default=uuid.uuid4,primary_key=True)
    company_id = models.StringField()
    link = models.StringField()
    label = models.StringField()
    company_name = models.StringField()
    company_cover = models.StringField()
    company_website = models.StringField()
    company_category = models.StringField()
    title = models.StringField()
    category = models.StringField()
    location = models.StringField()
    type_cooperation = models.StringField()
    work_experience = models.StringField()
    salary = models.StringField()
    description = models.StringField()
    company_about = models.StringField()
    gender = models.StringField()
    education = models.StringField()
    military_service = models.StringField()
    skills = models.ArrayField(base_field=models.StringField())
    date_last_crawl = models.StringField()
    publication_date = models.Int8Field()

    def __str__(self):
        return str(self.id)
