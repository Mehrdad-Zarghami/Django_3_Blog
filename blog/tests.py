from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import PostModel


class TestBlogPost(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        These samples are created only once, not before each test unlike setUp(self).
        If we change a test sample in a test, the change remains for next tests.
        """

        cls.user1 = User.objects.create(username='Mehrdad Test')
        cls.post1 = PostModel.objects.create(
            title='Test Title1',
            text='Description for Testing Post1',
            status=PostModel.STATUS_CHOICES[0][0],
            # status = 'pub'
            author=cls.user1,
        )
        cls.post2 = PostModel.objects.create(
            title='Test Title2',
            text='Description for Testing Post1',
            status=PostModel.STATUS_CHOICES[1][0],
            # status = 'drf'
            author=cls.user1,
        )

    # def setUp(self):
    #     self.user1 = User.objects.create(username='Mehrdad Test')
    #     self.post1 = PostModel.objects.create(
    #         title='Test Title1',
    #         text='Description for Testing Post1',
    #         status=PostModel.STATUS_CHOICES[0][0],
    #         # status = pub
    #         author=self.user1,
    #     )
    #     self.post2 = PostModel.objects.create(
    #         title='Test Title2',
    #         text='Description for Testing Post1',
    #         status=PostModel.STATUS_CHOICES[1][0],
    #         # status = 'drf'
    #         author=self.user1,
    #     )

    def test_posts_list_url(self):  # The name of a test function must start with 'test'
        # Check if '/blog/' url works or not
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_posts_list_url_by_name(self):
        # Check if the name of '/blog/' url which is "posts_list_page"  works or not
        response = self.client.get(reverse('posts_list_page'))
        self.assertEquals(response.status_code, 200)

    def test_post_title_on_posts_list_page(self):
        response = self.client.get(reverse('posts_list_page'))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_detail_page_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_page_url_by_name(self):
        response = self.client.get(reverse('post_detail_page', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_posst_title_on_post_detail_page(self):
        response = self.client.get(reverse('post_detail_page', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_does_not_exist(self):
        response = self.client.get(reverse('post_detail_page', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_posts_not_in_posts_list_page(self):
        response = self.client.get(reverse('posts_list_page'))
        self.assertContains(response, self.post1.title),
        self.assertNotContains(response, self.post2.title)
