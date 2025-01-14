# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnswerChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    problem = models.ForeignKey('Problems', models.DO_NOTHING, related_name='choices', blank=True, null=True)
    label = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=2048)
    default_score = models.BigIntegerField()
    description = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_choice'


class AnswerSheets(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    assistant = models.ForeignKey('Users', models.DO_NOTHING, related_name='answersheets_assistant_set', blank=True, null=True)
    assignment = models.ForeignKey('Assignments', models.DO_NOTHING, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    score = models.BigIntegerField(blank=True, null=True)
    adjusted_score = models.BigIntegerField(blank=True, null=True)
    submitted = models.DateTimeField(blank=True, null=True)
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_sheets'


class Answers(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    problem = models.ForeignKey('Problems', models.DO_NOTHING, blank=True, null=True)
    answer_sheet = models.ForeignKey(AnswerSheets, models.DO_NOTHING, blank=True, null=True)
    problem_order = models.BigIntegerField(blank=True, null=True)
    label = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=2048, blank=True, null=True)
    user_point = models.BigIntegerField(blank=True, null=True)
    assignment_point = models.BigIntegerField(blank=True, null=True)
    submitted = models.DateTimeField(blank=True, null=True)
    is_primary = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    hint = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class ArticleAssignment(models.Model):
    article = models.OneToOneField('Articles', models.DO_NOTHING, primary_key=True)  # The composite primary key (article_id, assignment_id) found, that is not supported. The first column is selected.
    assignment = models.ForeignKey('Assignments', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'article_assignment'
        unique_together = (('article', 'assignment'),)


class Articles(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey('Topics', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=True)
    published = models.DateTimeField()
    last_edited = models.DateTimeField()
    status = models.CharField(max_length=32)
    abstract = models.CharField(max_length=255, blank=True, null=True)
    number_viewed = models.BigIntegerField(blank=True, null=True)
    category = models.ForeignKey('Categories', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class AssignmentGroup(models.Model):
    assignment = models.OneToOneField('Assignments', models.DO_NOTHING, primary_key=True)  # The composite primary key (assignment_id, group_id) found, that is not supported. The first column is selected.
    group = models.ForeignKey('Groups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assignment_group'
        unique_together = (('assignment', 'group'),)


class AssignmentStudent(models.Model):
    assignment = models.OneToOneField('Assignments', models.DO_NOTHING, primary_key=True)  # The composite primary key (assignment_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assignment_student'
        unique_together = (('assignment', 'user'),)


class Assignments(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)
    difficulty = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignments'


class Baldan(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.OneToOneField('Users', models.DO_NOTHING, blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    last_score = models.BigIntegerField(blank=True, null=True)
    self_expectation = models.BigIntegerField(blank=True, null=True)
    goal_expectation = models.BigIntegerField(blank=True, null=True)
    number_solved = models.BigIntegerField(blank=True, null=True)
    number_skipped = models.CharField(max_length=256, blank=True, null=True)
    total_points = models.BigIntegerField(blank=True, null=True)
    total_assignment_points = models.BigIntegerField(blank=True, null=True)
    meta_data = models.TextField(blank=True, null=True)
    updated = models.BooleanField(blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    grade = models.ForeignKey('Grade', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baldan'


class BlueprintItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    blueprint = models.ForeignKey('Blueprints', models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey('Levels', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('Categories', models.DO_NOTHING, blank=True, null=True)
    num = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'blueprint_items'


class Blueprints(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'blueprints'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)
    category_order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoryTopic(models.Model):
    category_id = models.BigIntegerField(primary_key=True)  # The composite primary key (category_id, topic_id) found, that is not supported. The first column is selected.
    topic_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'category_topic'
        unique_together = (('category_id', 'topic_id'),)


class CollectionItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    collection = models.ForeignKey('Collections', models.DO_NOTHING, blank=True, null=True)
    problem = models.ForeignKey('Problems', models.DO_NOTHING, blank=True, null=True)
    problem_order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection_items'


class Collections(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, db_column='author', blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collections'


class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    comment = models.CharField(max_length=1024)
    resource = models.CharField(max_length=32, blank=True, null=True)
    comment_ip = models.CharField(max_length=32, blank=True, null=True)
    comment_date = models.DateTimeField(blank=True, null=True)
    comment_url = models.CharField(max_length=128, blank=True, null=True)
    mute_comments = models.BooleanField(blank=True, null=True)
    article = models.ForeignKey(Articles, models.DO_NOTHING, blank=True, null=True)
    problem = models.ForeignKey('Problems', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Formulas(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey('Topics', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    mute_comments = models.BooleanField()
    published = models.DateTimeField()
    last_edited = models.DateTimeField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formulas'


class Grade(models.Model):
    id = models.BigAutoField(primary_key=True)
    grade = models.BigIntegerField()
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'grade'


class GroupStudent(models.Model):
    group = models.OneToOneField('Groups', models.DO_NOTHING, primary_key=True)  # The composite primary key (group_id, student_id) found, that is not supported. The first column is selected.
    student = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_student'
        unique_together = (('group', 'student'),)


class Groups(models.Model):
    id = models.BigAutoField(primary_key=True)
    school = models.ForeignKey('Schools', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    grade = models.ForeignKey(Grade, models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    reg_code = models.OneToOneField('RegCodes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class KeywordFormula(models.Model):
    keyword = models.OneToOneField('Keywords', models.DO_NOTHING, primary_key=True)  # The composite primary key (keyword_id, formula_id) found, that is not supported. The first column is selected.
    formula = models.ForeignKey(Formulas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'keyword_formula'
        unique_together = (('keyword', 'formula'),)


class KeywordKeyword(models.Model):
    keyword_source = models.OneToOneField('Keywords', models.DO_NOTHING, db_column='keyword_source', primary_key=True)  # The composite primary key (keyword_source, keyword_target) found, that is not supported. The first column is selected.
    keyword_target = models.ForeignKey('Keywords', models.DO_NOTHING, db_column='keyword_target', related_name='keywordkeyword_keyword_target_set')

    class Meta:
        managed = False
        db_table = 'keyword_keyword'
        unique_together = (('keyword_source', 'keyword_target'),)


class KeywordProblem(models.Model):
    keyword = models.OneToOneField('Keywords', models.DO_NOTHING, primary_key=True)  # The composite primary key (keyword_id, problem_id) found, that is not supported. The first column is selected.
    problem = models.ForeignKey('Problems', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'keyword_problem'
        unique_together = (('keyword', 'problem'),)


class Keywords(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True, null=True)
    key_order = models.BigIntegerField(blank=True, null=True)
    grade = models.ForeignKey(Grade, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class Levels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'levels'

    def __str__(self):
        return self.name


class MessageUser(models.Model):
    message = models.OneToOneField('Messages', models.DO_NOTHING, primary_key=True)  # The composite primary key (message_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_user'
        unique_together = (('message', 'user'),)


class Messages(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    subject = models.CharField(max_length=128)
    body = models.TextField()
    type = models.CharField(max_length=255)
    status = models.BigIntegerField()
    remaining = models.BigIntegerField()
    total_recipients = models.BigIntegerField()
    urgency = models.BigIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'


class MixerItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    mixer = models.ForeignKey('Mixers', models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(Collections, models.DO_NOTHING, blank=True, null=True)
    collection_order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mixer_items'


class Mixers(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, db_column='author', blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mixers'


class Newkeys(models.Model):
    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newkeys'


class Points(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz_item = models.ForeignKey('QuizItems', models.DO_NOTHING, blank=True, null=True)
    label = models.CharField(max_length=26, blank=True, null=True)
    point = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'points'


class ProblemComments(models.Model):
    problem = models.OneToOneField('Problems', models.DO_NOTHING, primary_key=True)  # The composite primary key (problem_id, comment_id) found, that is not supported. The first column is selected.
    comment = models.OneToOneField(Comments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'problem_comments'
        unique_together = (('problem', 'comment'),)


class Problems(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.ForeignKey(Levels, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    answer = models.CharField(max_length=1024, blank=True, null=True)
    last_edited = models.DateTimeField(blank=True, null=True)
    rendering = models.CharField(max_length=32)
    mute_comments = models.BooleanField(blank=True, null=True)
    success_rate = models.FloatField(blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problems'


class ProductComments(models.Model):
    solution = models.OneToOneField('Products', models.DO_NOTHING, primary_key=True)  # The composite primary key (solution_id, comment_id) found, that is not supported. The first column is selected.
    comment = models.ForeignKey(Comments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_comments'
        unique_together = (('solution', 'comment'),)


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    picture_url = models.CharField(max_length=512)
    remaining = models.BigIntegerField()
    price = models.BigIntegerField()
    status = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Provinces(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'provinces'


class Purchases(models.Model):
    id = models.BigAutoField(primary_key=True)
    costumer = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    number_of_items = models.BigIntegerField()
    unit_price = models.BigIntegerField()
    total_price = models.BigIntegerField()
    purchase_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchases'


class QuizGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)
    order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_group'


class QuizGroupItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(QuizGroup, models.DO_NOTHING, blank=True, null=True)
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING, blank=True, null=True)
    quiz_order = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_group_items'


class QuizItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.ForeignKey('Quizzes', models.DO_NOTHING, blank=True, null=True)
    problem = models.ForeignKey(Problems, models.DO_NOTHING, blank=True, null=True)
    problem_order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_items'


class Quizzes(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    grade = models.ForeignKey(Grade, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True, null=True)
    status = models.BigIntegerField()
    default_time_limit = models.BigIntegerField(blank=True, null=True)
    average_score = models.BigIntegerField(blank=True, null=True)
    standard_deviation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    score_table = models.CharField(max_length=512, blank=True, null=True)
    is_sample = models.BooleanField(blank=True, null=True)
    is_public = models.BooleanField(blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quizzes'


class RegCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    num_days = models.BigIntegerField()
    price = models.BigIntegerField()
    activated = models.DateTimeField(blank=True, null=True)
    code_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg_codes'


class Results(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('Users', models.DO_NOTHING, blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    score = models.BigIntegerField(blank=True, null=True)
    adjusted_score = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'


class Schools(models.Model):
    id = models.BigAutoField(primary_key=True)
    province = models.ForeignKey(Provinces, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'schools'


class SolutionComments(models.Model):
    solution = models.OneToOneField('Solutions', models.DO_NOTHING, primary_key=True)  # The composite primary key (solution_id, comment_id) found, that is not supported. The first column is selected.
    comment = models.OneToOneField(Comments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'solution_comments'
        unique_together = (('solution', 'comment'),)


class SolutionFormula(models.Model):
    solution = models.OneToOneField('Solutions', models.DO_NOTHING, primary_key=True)  # The composite primary key (solution_id, formula_id) found, that is not supported. The first column is selected.
    formula = models.ForeignKey(Formulas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'solution_formula'
        unique_together = (('solution', 'formula'),)


class Solutions(models.Model):
    id = models.BigAutoField(primary_key=True)
    problem = models.ForeignKey(Problems, models.DO_NOTHING)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    mute_comments = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'solutions'


class TeacherGroup(models.Model):
    teacher = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (teacher_id, group_id) found, that is not supported. The first column is selected.
    group = models.ForeignKey(Groups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teacher_group'
        unique_together = (('teacher', 'group'),)


class TopicKeyword(models.Model):
    topic_id = models.BigIntegerField(primary_key=True)  # The composite primary key (topic_id, keyword_id) found, that is not supported. The first column is selected.
    keyword = models.ForeignKey(Keywords, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'topic_keyword'
        unique_together = (('topic_id', 'keyword'),)


class Topics(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True, null=True)
    weight = models.BigIntegerField(blank=True, null=True)
    topic_order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topics'


class UserFormula(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    formula = models.ForeignKey(Formulas, models.DO_NOTHING, blank=True, null=True)
    formula_order = models.BigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=512, blank=True, null=True)
    number_of_view = models.BigIntegerField(blank=True, null=True)
    last_view = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_formula'


class UserProblem(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    problem = models.ForeignKey(Problems, models.DO_NOTHING, blank=True, null=True)
    problem_order = models.BigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=512, blank=True, null=True)
    number_of_view = models.BigIntegerField(blank=True, null=True)
    last_view = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_problem'


class UserTopic(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey(Topics, models.DO_NOTHING, blank=True, null=True)
    l10_rate = models.FloatField(blank=True, null=True)
    success_rate = models.FloatField(blank=True, null=True)
    disabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_topic'


class UserUploads(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=64)
    upload_date = models.DateTimeField(blank=True, null=True)
    quiz = models.ForeignKey(Quizzes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_uploads'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    plain_password = models.CharField(max_length=128, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True, null=True)
    facebook_id = models.CharField(max_length=60, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    picture_url = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(unique=True, max_length=60, blank=True, null=True)
    telephone_number = models.CharField(max_length=30, blank=True, null=True)
    balance = models.BigIntegerField(blank=True, null=True)
    last_login = models.DateTimeField()
    created = models.DateTimeField(blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    is_blocked = models.BooleanField()
    marketing_email = models.BooleanField()
    number_solved = models.BigIntegerField(blank=True, null=True)
    success_rate = models.FloatField(blank=True, null=True)
    token = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
