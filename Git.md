# Git 활용 가이드

이 문서는 프로젝트의 Git 활용 가이드라인을 제공합니다.





## 커밋 메시지 규칙

커밋 메시지는 다음과 같은 구조를 따릅니다:

```
🔥 Type : title

[Description]

[Resolves] : #issueNumber
```

### 커밋 메시지 구성 요소

1. **이모지(Gitmoji)**: 변경 유형을 직관적으로 나타내는 이모지
2. **Type**: 변경 유형 (첫 글자는 대문자로 작성)
3. **title**: 변경 사항을 간결하게 설명하는 제목
4. **Description**: (선택 사항) 변경 사항에 대한 자세한 설명
5. **Resolves**: (선택 사항) 관련된 이슈 번호

### 커밋 타입(Type) 가이드라인

타입의 첫 글자는 대문자로 작성합니다:

* **Feat**: 새로운 기능 추가
  * 예: `✨ Feat : Add search functionality to header`
* **Fix**: 버그 수정
  * 예: `🐛 Fix : Fix infinite loop in pagination`
* **Docs**: 문서 수정
  * 예: `📝 Docs : Update README with commit guidelines`
* **Style**: 코드 스타일 변경
  * 예: `💄 Style : Format user service according to style guide`
* **Design**: UI 디자인 변경
  * 예: `🎨 Design : Update primary button styles`
* **Refactor**: 코드 리팩토링
  * 예: `♻️ Refactor : Simplify order processing logic`
* **Test**: 테스트 관련
  * 예: `✅ Test : Add integration tests for auth flow`
* **Build**: 빌드 관련
  * 예: `👷 Build : Update webpack configuration`
* **Perf**: 성능 개선
  * 예: `⚡ Perf : Optimize image loading in feed`
* **Chore**: 자잘한 수정
  * 예: `🔧 Chore : Update dependencies`
* **Rename**: 파일/폴더명 수정
  * 예: `🚚 Rename : Rename UserComponent to UserProfile`
* **Remove**: 파일 삭제
  * 예: `🔥 Remove : Remove unused utility functions`
* **Revert**: 되돌리기
  * 예: `⏪ Revert : Revert "feat: Add new feature"`

## 깃모지 (Gitmoji) 사용

커밋 메시지에는 변경 유형을 나타내는 깃모지를 사용합니다. 공식 깃모지 목록과 의미는 다음 사이트를 참조하세요:

[https://gitmoji.dev/](https://gitmoji.dev/)

## 예시

```
✨ Feat : 회원가입 기능 추가

사용자 회원가입 화면과 API 연동 기능을 구현했습니다.
- 이메일 중복 확인 기능 추가
- 비밀번호 강도 체크 로직 구현
- 회원가입 성공 시 로그인 페이지로 리다이렉트

Resolves : #42
```

## 참고 사항

- 커밋은 작고 논리적인 단위로 나누어 작성해주세요.
- 커밋 메시지는 한글 또는 영어로 일관성 있게 작성해주세요.