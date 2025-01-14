from rest_framework import serializers
from .models import Problems, AnswerChoice

class AnswerChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = AnswerChoice
        fields = ['id', 'label', 'value', 'default_score', 'description']

class ProblemSerializer(serializers.ModelSerializer):
    choices = AnswerChoiceSerializer(many=True)

    class Meta:
        model = Problems
        fields = ['id', 'type', 'title', 'statement', 'answer', 'rendering', 'level', 'choices', 'is_published']

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.title = validated_data.get('title', instance.title)
        instance.statement = validated_data.get('statement', instance.statement)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.rendering = validated_data.get('rendering', instance.rendering)
        instance.level = validated_data.get('level', instance.level)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.save()

        # Handle choices
        choices_data = validated_data.get('choices', [])
        for choice_data in choices_data:
            if 'id' in choice_data and choice_data['id']:
                # Update existing choice
                choice = AnswerChoice.objects.get(id=choice_data['id'])
                choice.label = choice_data.get('label', choice.label)
                choice.value = choice_data.get('value', choice.value)
                choice.default_score = choice_data.get('default_score', choice.default_score)
                choice.description = choice_data.get('description', choice.description)
                choice.save()
            else:
                AnswerChoice.objects.create(
                    problem=instance,
                    label=choice_data.get('label'),
                    value=choice_data.get('value'),
                    default_score=choice_data.get('default_score'),
                    description=choice_data.get('description')
                )
        return instance
