from rest_framework import mixins, viewsets, exceptions
from rest_framework.decorators import list_route
from rest_framework.response import Response

from record.models import ChannelRecord, RecommendRecord
from record.serializers import ChannelRecordSerializer, RecommendRecordSerializer
from student.models import StudentInfo


class ChannelRecordView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = ChannelRecord.objects.all()
    serializer_class = ChannelRecordSerializer


class RecommendRecordView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = RecommendRecord.objects.all()
    serializer_class = RecommendRecordSerializer

    @list_route()
    def success(self, request):
        student = request.user
        result = RecommendRecord.objects.filter(inviter=student.id, status=True).distinct().values('invitee')
        invitee_list = [data['invitee'] for data in result]
        # 然后去学校信息中查询是否已缴费成功
        student_list = StudentInfo.objects.filter(id__in=invitee_list).values('id', 'name', 'student_status')
        result_data = list(student_list)
        for data in result_data:
            if data['student_status'] == 'SUPPLY_ORDER':
                data['student_status'] = '已提交订单'
            elif data['student_status'] == 'TO_PAYMENT_CONFIRM':
                data['student_status'] = '待缴费确认'
            else:
                data['student_status'] = '缴费确认成功'
        return Response(result_data)

    @list_route()
    def success_by_student(self, request):
        student_id = request.query_params.get('student_id')
        tag = request.query_params.get('tag', False)
        if not student_id:
            raise exceptions.ValidationError('参数student_id为空')
        result = RecommendRecord.objects.filter(inviter=student_id, status=True).distinct().values('invitee',
                                                                                                   'create_time')
        invitee_list = [data['invitee'] for data in result]
        invite_at_result = {data['invitee']: data['create_time'] for data in result}
        # 然后去学校信息中查询是否已缴费成功
        student_list = StudentInfo.objects.filter(id__in=invitee_list).values('id', 'name', 'student_status', 'cschool',
                                                                              'last_login', 'cc', 'server')
        result_data = list(student_list)
        for data in result_data:
            data['invite_time'] = invite_at_result[str(data['id'])]
            if data['student_status'] == 'SUPPLY_ORDER':
                data['student_status'] = '已提交订单'
            elif data['student_status'] == 'TO_PAYMENT_CONFIRM':
                data['student_status'] = '待缴费确认'
            else:
                data['student_status'] = '缴费确认成功'
        result_data = sorted(result_data, key=lambda student: student['invite_time'], reverse=True)
        if tag and len(result_data) > 5:
            return Response(result_data[:5])
        return Response(result_data)
