import random


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    """
    Evaluates the submission for a particular challenge phase and returns score
    Arguments:

        `test_annotations_file`: Path to test_annotation_file on the server
        `user_submission_file`: Path to file submitted by the user
        `phase_codename`: Phase to which submission is made

        `**kwargs`: keyword arguments that contains additional submission
        metadata that challenge hosts can use to send slack notification.
        You can access the submission metadata
        with kwargs['submission_metadata']

        Example: A sample submission metadata can be accessed like this:
        >>> print(kwargs['submission_metadata'])
        {
            'status': u'running',
            'when_made_public': None,
            'participant_team': 5,
            'input_file': 'https://abc.xyz/path/to/submission/file.json',
            'execution_time': u'123',
            'publication_url': u'ABC',
            'challenge_phase': 1,
            'created_by': u'ABC',
            'stdout_file': 'https://abc.xyz/path/to/stdout/file.json',
            'method_name': u'Test',
            'stderr_file': 'https://abc.xyz/path/to/stderr/file.json',
            'participant_team_name': u'Test Team',
            'project_url': u'http://foo.bar',
            'method_description': u'ABC',
            'is_public': False,
            'submission_result_file': 'https://abc.xyz/path/result/file.json',
            'id': 123,
            'submitted_at': u'2017-03-20T19:22:03.880652Z'
        }
    """
    # --- #
    # test_annotation_file == challenge_config.yaml에서 설정한 정답 파일 #
    # user_submission_file == 유저가 사이트에서 업로드할 파일 #
    # phase_codename = challenge_config에서 설정하였음 #
    # --- #

    # --- #
    # 아래 output에 결과를 입력하고 return하면 사이트내 리더보드에 올라갑니다. #
    # output의 양식은 본인이 challenge_config.yaml에서 설정한 dataset_splits과 leaderboard(평가 메트릭)에 맞추시면 됩니다. #
    output = {}
    # --- #
    
    # --- #
    # test_annotation_file(json 형식)과 user_submission_file(json 형식)을 비교하는 평가 코드는 이 위치에 넣어주세요. #
    # phase_codename을 challenge_config에서 설정하지 않았다면, 굳이 반복문으로 나눌 필요는 없습니다. #
    # challenge_config의 dataset_splits과 leaderboard의 labels를 기반으로 output["result"]에 결과값을 입력하면 됩니다. #
    # 해당 repo의 issue #3에 @chldydgh4687님이 예시를 올려두었으니, 해당 내용을 참고하셔도 좋습니다...! #
    # --- #

    if phase_codename == "dev":
        # --- #
        # "dataset_splits" : { leaderboard's labels : 000 } #
        # 와 같은 형태로 입력해야합니다. #
        # challenge_config.yaml의 이름과 동일한지 꼭 확인해주세요 # 
        print("Evaluating for Dev Phase")
        output["result"] = [
            {
                "train_split": {
                    "Metric1": random.randint(0, 99),
                    "Metric2": random.randint(0, 99),
                    "Metric3": random.randint(0, 99),
                    "Total": random.randint(0, 99),
                }
            }
        ]
        # --- #
        # To display the results in the result file
        output["submission_result"] = output["result"][0]["train_split"]
        print("Completed evaluation for Dev Phase")
    elif phase_codename == "test":
        print("Evaluating for Test Phase")
        output["result"] = [
            {
                "train_split": {
                    "Metric1": random.randint(0, 99),
                    "Metric2": random.randint(0, 99),
                    "Metric3": random.randint(0, 99),
                    "Total": random.randint(0, 99),
                }
            },
            {
                "test_split": {
                    "Metric1": random.randint(0, 99),
                    "Metric2": random.randint(0, 99),
                    "Metric3": random.randint(0, 99),
                    "Total": random.randint(0, 99),
                }
            },
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]
        print("Completed evaluation for Test Phase")
    return output
