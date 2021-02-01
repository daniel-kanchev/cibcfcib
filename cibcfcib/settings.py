BOT_NAME = 'cibcfcib'
SPIDER_MODULES = ['cibcfcib.spiders']
NEWSPIDER_MODULE = 'cibcfcib.spiders'
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'cibcfcib.pipelines.DatabasePipeline': 300,
}
