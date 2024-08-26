import { BlogPostsPreview } from "@/components/BlogPostPreview";
import { BlogPostsPagination } from "@/components/BlogPostsPagination";
import { Footer } from "@/components/Footer";
import { Header } from "@/components/Header";
import { wisp } from "@/lib/wisp";


const Page = async ({ 
  searchParams,
}: {
  searchParams: { [key: string]: string | string[] | undefined };
}) => {
  const page = searchParams.page ? parseInt(searchParams.page as string) : 1;
  const result = await wisp.getPosts({ limit: 6, page });
  const res = await fetch('http://4d2d:8080/api/offers?format=json').then((res) => {
      return res
  }
  )

  const json = await res.json();

  return (
    <div className="container mx-auto px-5 mb-10">
      <Header />
      {/* <h1>{json[0].title}</h1> */}
      <BlogPostsPreview posts={json} />
      <BlogPostsPagination pagination={result.pagination} />
      <Footer />
    </div>
  );
};

export default Page;
